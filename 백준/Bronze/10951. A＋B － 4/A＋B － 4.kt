import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    while(true){
        try{
            var A = nextInt()
            var B = nextInt()

            println(A+B)
        }catch (e: NoSuchElementException){break}
    }
}