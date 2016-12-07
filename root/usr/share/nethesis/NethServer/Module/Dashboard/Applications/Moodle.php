<?php
namespace NethServer\Module\Dashboard\Applications;

/*
 * Copyright (C) 2013 Nethesis S.r.l.
 *
 * This script is part of NethServer.
 *
 * NethServer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * NethServer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with NethServer.  If not, see <http://www.gnu.org/licenses/>.
 */

/**
 * Moodle dashboard application widget
 *
 * @author Alain Reguera Delgado
 */
class Moodle extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{

    public function getName()
    {
        return "Moodle";
    }

    public function getInfo()
    {
        // Set host value based on database configuration
        if ($this->getPlatform()->getDatabase('configuration')->getProp('moodle','host') != "") {
            $host = $this->getPlatform()->getDatabase('configuration')->getProp('moodle','host');
        } else {
            $host = explode(':', $_SERVER['HTTP_HOST']);
            $host = $host[0];
        }

        // Set path value based on database configuration
        $path = $this->getPlatform()->getDatabase('configuration')->getProp('moodle','path');
        $apacheConf = $this->getPlatform()->getDatabase('configuration')->getProp('moodle','apacheConf'); 

        // Set url value based on apache configuration
        if ( $apacheConf == "virtualhost" )
            $url = "https://" . $host;
        else
            $url = "https://" . $host . "/$path";

        return array(
            'url' => $url
        );
    }
}
