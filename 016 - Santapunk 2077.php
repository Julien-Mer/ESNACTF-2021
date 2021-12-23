<?php

while(true) {
	$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
	$res = socket_connect($socket, "192.168.120.11", 46105);
	if (!$socket)  echo "$errstr ($errno)<br />\n";
	else {
		$out = '';
		$weapon = "Lame rouillée"; 
		while ($out = socket_read($socket, 2048)) {
			echo $out;
			$re = '/You find a (.*)\. Type/ms';
			$re2 = '/HP ([0-9]+)/ms';
			if(strpos($out, "ESNA")) {
				echo "GO"."\n";
			} if(strpos($out, "MORE ARMOR")) {
				echo "Super de l'armure !"."\n";
				move($out, $socket);
			} if(strpos($out, "WEAPONERY BETTER")) {
				echo "Super pour les dommages !"."\n";
				move($out, $socket);
			} else if(strpos($out, "DMG BOOST")) {
				echo "Super du dommage !"."\n";
				move($out, $socket);
			} else if(strpos($out, "flag")) {
				sleep(2);
			} else if(preg_match_all($re2, $out, $matchess, PREG_SET_ORDER, 0)) {
				send("BACK", $socket);
			} else if(strpos($out, "cannot go back")) {
				echo "Go le combattre"."\n";
				send("FIGHT", $socket); // Obligé de combattre
			} else if(strpos($out, "TRAP") || strpos($out, "You died")) {
				echo "oof";
				socket_close($socket);
				continue;
			} else if(strpos($out, "ton nom")) {
				send("Ok", $socket);
			} else if(strpos($out, "Assign to STR")) {
				send("7", $socket);
			} else if(strpos($out, "Assign to INT")) {
				send("1", $socket);
			} else if(strpos($out, "1. Jouer")) {
				send("1", $socket);
			} else if(strpos($out, "You lose")) {
				echo "Perte de HP ...\n";
				move($out, $socket);
			} else if(strpos($out, "points available")) {
			} else if(preg_match_all($re, $out, $matches, PREG_SET_ORDER, 0)) {
				echo "Arme trouvée !"."\n";
				$choice = EquipOrNot($weapon, $matches);
				if($choice !== $weapon) {
					$weapon = $choice;
					send("EQUIP", $socket);
				} else {
					move($out, $socket);
				}
			} else if(strpos($out, "directions")){
				echo "commande inconnues\n";
				move($out, $socket);
			}
		}
	}
	socket_close($socket);
}

function EquipOrNot($weapon, $output) {
	$weapons = [
		"Lame rouillée",
		"Epée de pirate",
		"Bonne épée",
		"Dague",
		"Pistolet",
		"Sabre laser",
		"RPG-7",
		"Excalibur",
	];
	$indexWeapon = array_search($weapon, $weapons);
	$new = $output[0][1];
	$indexNew = array_search($new, $weapons);
	if($indexNew === false) {
		sleep(30);
		echo "??? weapon ???\n";
	}
	if($indexNew > $indexWeapon) {
		return $new;
	} else {
		return $weapon;
	}
}

function move($out, $socket) {
	$re = '/(\'([A-Z])\')+/m';
	preg_match_all($re, $out, $matches, PREG_SET_ORDER, 0);
	$dirs = [];
	foreach($matches as $key=>$match)
		$dirs[] = $match[2];
	$choice = $dirs[array_rand($dirs)];
	send("GOTO ".$choice, $socket);
}

function send($in, $socket) {	
	$in = $in."\n";
	echo "-> ".$in."\n";
	socket_write($socket, $in, strlen($in));
}