<?php
interface AdvancedArithmetic{
            public function divisorSum($n);
        }

public function divisorSum($number) {
        int $sum = 0
        for ($i = 1; i <=$n; $i++ {
                if $number % 2
                }        
        
        }



$n=intval(fgets(STDIN));
$myCalculator=new Calculator();
if($myCalculator instanceof AdvancedArithmetic)//checking if Calculator has implemented AdvancedArithemtic
{
            $sum=$myCalculator->divisorSum($n);
                echo "I implemented: AdvancedArithmetic\n".$sum;
}
else
{
            echo "Wrong answer";// You will get this output if you dont implement
}
?>
