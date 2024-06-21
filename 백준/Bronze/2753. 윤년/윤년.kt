import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    val year = nextInt()
    var answer = 0

    if (year % 4 == 0)
        if (year % 100 != 0 || year % 400 == 0){
            answer = 1
        }

    print(answer)
}