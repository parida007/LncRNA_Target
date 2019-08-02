<?php
/**
 * Created by PhpStorm.
 * User: lenovo
 * Date: 13-06-2019
 * Time: 20:54
 */


    $ml_model='Logistic_Regression.sav';
    exec('python Main_File.py '.$ml_model);
    $myfile = fopen("Binding_Probability.txt", "r") or die("Unable to open file!");
    echo '<h1>'.fread($myfile,filesize("Binding_Probability.txt")).'</h1>';
?>