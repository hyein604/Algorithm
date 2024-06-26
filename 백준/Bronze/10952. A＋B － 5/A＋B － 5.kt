import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    while(true){
        var A = nextInt()
        var B = nextInt()

        if(A == 0 && B == 0) break

        println(A+B)
    }
}