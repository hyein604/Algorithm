import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    var N = nextInt()

    for (i:Int in 1..N){
        var A = nextInt()
        var B = nextInt()

        println("${A + B}")
    }
}