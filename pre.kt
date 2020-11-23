fun sum(first: String, second: String, sign: String): String {
    return "(" + first + sign + second + ")"
}

fun isNumber(s: String): Boolean {
    if (s.isEmpty()) return false
    for (symbol in s) {
        if (!symbol.isDigit()) {
            return false
        }
    }
    return true
}

fun isSign(str: String): Boolean {
    val ops = arrayOf("+", "-", "*", "/")
    for (op in ops) {
        if (op.equals(str)) return true
    }
    return false
}

fun pop(s: MutableList<String>): String {

    var result = s.get(s.lastIndex)
    s.removeAt(s.lastIndex)
    return result
}

fun main(args: Array<String>) {
    var input: String? = readLine()

    if (!input.isNullOrEmpty()) {
        var symbols = ArrayList<String>(input?.split(' '))
        val buffer = mutableListOf<String>()
        val numbers = mutableListOf<String>()
        val signs = mutableListOf<String>()

        for (symbol in symbols.reversed()) {
            if (isSign(symbol)) {
                if (buffer.lastIndex>=1){
                    var first=  pop(buffer)
                    var second= pop(buffer)
                    var str = sum(first, second, symbol)
                    buffer.add(str)
                }
                else{
                    println("Я не вижу значений для символа! Проверь то что ты вводишь :(")
                    buffer.add(symbol)//закидываем символ в буфер чтоб не выводить ошибку дважды
                    break
                }
            }else if (isNumber(symbol)) {
                buffer.add(symbol)
            }
        }
        if (buffer.lastIndex==0){
            println(buffer[0])
        }
        else{
            if (!isSign(buffer[1])) {//если в буфере знак, значит ошибка уже была выше
                println("Кажется, ты ввёл больше числе чем надо.. Я так не работаю(")
            }
        }
    }
}