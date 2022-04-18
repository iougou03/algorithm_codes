public class ThreadExample {
    public static void main(String[] args) {
        Runnable task = () -> {
            for(int i = 0 ; i < 5 ; i++) {
                System.out.println("Hello, Lambda Runnable");
            }
        };

        Thread thread = new Thread(task);
        thread.start();

        try {
            thread.join();
        } catch (InterruptedException e) {
            System.out.println("Parent Thread is Interrupted");
        }
        System.out.println("Hello My child");
    }
}
