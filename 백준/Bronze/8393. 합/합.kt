import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    var N = nextInt()

    var answer = 0
    for (i:Int in 1..N)
        answer += i

    print(answer)
}