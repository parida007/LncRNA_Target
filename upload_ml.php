<?php
    exec("rm IS_RUNNING.txt");


    
    exec("/home/sibun/anaconda3/bin/python Parallel_Check.py");
    $handle = fopen("IS_RUNNING.txt", "r");
    if ($handle) {
        while (($line = fgets($handle)) !== false) {
            $cont=trim($line);
          }
    
        fclose($handle);
    }
    if($cont!=="NO"){
        require('Exception_Parallel.php');
        exit(0);
    }



$name = 'query';
$ext = '.fa';
    $saveto = "$name$ext";
    move_uploaded_file($_FILES['query']['tmp_name'], $saveto);
    $typeok = TRUE;

$name1 = 'target';
$ext1 = '.fa';
    $saveto = "$name1$ext1";
    move_uploaded_file($_FILES['target']['tmp_name'], $saveto);
    $typeok = TRUE;

    include("Cleaning_Ops_1.php");	

    exec("/home/sibun/anaconda3/bin/python Multiline_Convert.py query.fa");
    exec("/home/sibun/anaconda3/bin/python Multiline_Convert.py target.fa");


 /*   
    exec("sudo python Coding_Potential.py");
    exec("/home/sibun/anaconda3/bin/python Preprocess_Coding_Potential.py");

    $handle = fopen("result_query.txt", "r");
    if ($handle) {
        while (($line = fgets($handle)) !== false) {
            if(trim($line)!=="Non-coding"){
                header('Location: Exception_Handling_Files.php');
                $cont=0;

            }
          }
    
        fclose($handle);
    }


    $handle = fopen("result_target.txt", "r");
    if ($handle) {
        while (($line = fgets($handle)) !== false) {
            if(trim($line)!=='Coding'){
                header('Location: Exception_Handling_Files.php');
                $cont=0;

            }
          }
    
        fclose($handle);
    }

*/
		
    exec("/home/sibun/anaconda3/bin/python Count_Seq.py");
    $handle = fopen("count_q_seq.txt", "r");
    if ($handle) {
        while (($line = fgets($handle)) !== false) {
            if(intval(trim($line))>2){
                require('Exception_Handling_Seq_Num.php');
                exit(0);

            }
          }
    
        fclose($handle);
    }


    $handle = fopen("count_t_seq.txt", "r");
    if ($handle) {
        while (($line = fgets($handle)) !== false) {
            if(intval(trim($line))>2){
                require('Exception_Handling_Seq_Num.php');
                exit(0);

            }

          }
    
        fclose($handle);
    }

   	

    
    if($cont==='NO'){
      exec("sudo python Main.py");
    
      $flag = file_exists('LncRNA_MRNA_Binding_Prediction.csv');
      if ($flag) {
        header('Location: Output_Php.php');
      } else {
        header('Location: Exception_Handling.php');  
      }
  }
    
?>
