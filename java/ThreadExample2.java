public class ThreadExample2 {
    
    public static void main(String[] args) {
        Runnable task = () -> {
            try {
                while (true){
                    System.out.println("Hello, Lambda Runnable");
                    Thread.sleep(500);
                }
            } catch (InterruptedException ie) {
                System.out.println("Thead Interrupted");
            }
        };

        Thread thread = new Thread(task);
        thread.start();
        try {
            Thread.sleep(1000);
        } catch (Exception e) {
        }
        thread.interrupt();
        System.out.println("End all Thread");
    }
}
