import java.util.Scanner

fun main() = with(Scanner(System.`in`)) {
    var X = nextInt()   // 영수증에 적힌 총 금액
    var N = nextInt()   // 물건 종류 수
    var total = 0

    for(i: Int in 1..N){
        var A = nextInt()   // 물건의 가격
        var B = nextInt()   // 물건의 개수

        total += A*B
    }

    if(X == total) println("Yes")
    else println("No")
}