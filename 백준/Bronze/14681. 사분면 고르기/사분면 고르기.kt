import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val x = nextInt()
    val y = nextInt()

    if (x > 0 && y > 0) print(1)
    else if (x < 0 && y > 0) print(2)
    else if (x < 0 && y < 0) print(3)
    else print(4)
}