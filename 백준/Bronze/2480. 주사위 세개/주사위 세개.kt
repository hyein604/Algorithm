import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val A = nextInt()
    val B = nextInt()
    val C = nextInt()

    var answer = 0

    if (A == B && B == C && A == C)
        answer = 10000 + A * 1000
    else if (A == B || B == C || A == C)
        if (A == B) answer = 1000 + A * 100
        else if (B == C) answer = 1000 + B * 100
        else answer = 1000 + C * 100
    else
        answer = listOf(A, B, C).max() * 100

    print(answer)
}