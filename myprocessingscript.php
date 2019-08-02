<?php header("Location: final_energy_data.html");


if(isset($_POST['field1']) && isset($_POST['field2'])&& isset($_POST['field0'])) {
    $data = $_POST['field1']; 
    $data1 = $_POST['field2'] ;
    $data2 = $_POST['field0'];
 $fp = fopen('query.fa', 'w');
fwrite($fp, $data);
fclose($fp);
$fr= fopen('target.fa', 'w');
fwrite($fr, $data1);
fclose($fr);

$fm=fopen('max_base_span.txt','w');
fwrite($fm, $data2);
fclose($fm);

  exec("python cal_modified_hybrid_energy1.py");  
												
}
else {
   die('no post data to process');
    
}


?>
