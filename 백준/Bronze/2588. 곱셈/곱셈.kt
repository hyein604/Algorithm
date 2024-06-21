fun main() {
    var input1 = readLine()!!.toInt()
    var input2 = readLine()!!
    var nums = input2.map{it.toString().toInt()}


    print("""${input1 * nums[2]}
        |${input1 * nums[1]}
        |${input1 * nums[0]}
        |${input1 * nums[2] + input1 * nums[1] * 10 + input1 * nums[0] * 100}
    """.trimMargin())
}