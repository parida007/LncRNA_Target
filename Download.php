<?php
header('Content-Type: application/csv');
header('Content-Disposition: attachment; filename=LncRNA_MRNA_Binding_Prediction.csv');
header('Pragma: no-cache');
readfile("LncRNA_MRNA_Binding_Prediction.csv");