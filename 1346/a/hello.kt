import kotlin.math.*

fun main(args: Array<String>) {
		val t = readLine()!!.toInt()
			repeat(t){
				val (n, k) = readLine()!!.split(" ").map { it.toInt() }
				val my = n/(1+k+k.pow(2)+k.pow(3))
				println(my + " " + my*k + " " + my*k.pow(2) + " " + my*k.pow(3))
			}
}

