import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    var N = nextInt()

    for(i: Int in 1..N){
        for(j: Int in 1..i){
            print("*")}
        print("\n")}
}