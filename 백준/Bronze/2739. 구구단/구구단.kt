import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    var N = nextInt()

    for (i:Int in 1..9)
        println("$N * $i = ${N*i}")
}