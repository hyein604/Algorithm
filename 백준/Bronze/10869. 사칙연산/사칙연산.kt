fun main(){
    var input = readLine()!!
    var result = input.split(' ')
    println(result[0].toInt() + result[1].toInt())
    println(result[0].toInt() - result[1].toInt())
    println(result[0].toInt() * result[1].toInt())
    println(result[0].toInt() / result[1].toInt())
    println(result[0].toInt() % result[1].toInt())
}