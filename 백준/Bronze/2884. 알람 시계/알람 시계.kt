import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val H = nextInt()
    val M = nextInt()

    if (M - 45 < 0){
        if (H == 0) print("23 ${60 - 45 + M}")
        else print("${H - 1} ${60 - 45 + M}")
    }
    else print("${H} ${M - 45}")
}