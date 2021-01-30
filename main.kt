import kotlin.concurrent.thread
import kotlin.system.measureTimeMillis
import java.util.concurrent.locks.ReentrantLock

fun main(args: Array<String>){
    val lock = ReentrantLock()
    val thread1 = thread {
        for(i in 1..10){
            //lock.lock();//Оставил на случай если спроосите как их разделить
            if(i%2==0){
                println(i)
            }
            //lock.unlock()

        }
    }
    val thread2 = thread {
        for(i in 1..10){
            //lock.lock();
            if(i%2!=0){
                println(i)
            }
            //lock.unlock()

        }
    }
    thread1.join()
    thread2.join()
}