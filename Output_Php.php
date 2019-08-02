<?php
// Open the file for reading
if (($h = fopen("LncRNA_MRNA_Binding_Prediction.csv", "r")) !== FALSE)
{
    // Each line in the file is converted into an individual array that we call $data
    // The items of the array are comma separated
    $line=0;
    echo "<table border='3'>";
    $h_r_start='';
    $h_r_end='';
    while (($data = fgetcsv($h)) !== FALSE)
    {
        // Each individual array is being pushed into the nested array
        $num = count($data);
        echo "<tr>";
        for ($c=0; $c < $num; $c++) {
            if ($line==0)
            {
                $h_r_start="<th>";
                $h_r_end="</th>";
            }
            else{
                $h_r_start="<td>";
                $h_r_end="</td>";
            }
			
			
            if(($c>=10)&&($c<24)){
                continue;
            }
			
			
            if ($c<2){
                $color='black';
                $size=4;
            }
            else if ($c<10){
                $color='blue';
                $size=4;
            }
            else{
                $color='green';
                $size=4;
            }
            echo $h_r_start."<font color=$color size=$size>".$data[$c]."</font>".$h_r_end;
        }
        echo   "</tr>";
        $line=$line+1;

    }
    echo "</table>";

    // Close the file
    fclose($h);
}
echo "<a href='Download.php'><font size='5'> Click here to download an example of the Output file</font></a>";
echo "<br/><br/>";
echo "<a href='final_energy_data.html'><font size='5'> Go to Final Energy Data File</font></a>";
echo "<br/><br/>";
echo "<a href='Cleaning_Ops.php'><font size='5'> Go to Home Page</font></a>";
