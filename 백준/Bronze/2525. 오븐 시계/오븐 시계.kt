import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val A = nextInt()   // 현재 시
    val B = nextInt()   // 현재 분
    val C = nextInt()   // 걸리는 분

    val D = B + C

    if(A + D / 60 >= 24) print("${(A + D / 60) - 24} ${D % 60}")
    else print("${A + D / 60} ${D % 60}")
}