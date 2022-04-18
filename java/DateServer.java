import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class DateServer {
    public static void main(String[] args) throws Exception{
        @SuppressWarnings("resource")
        ServerSocket server = new ServerSocket(8080);

        while (true) {
            System.out.println("Listening...");
            Socket client = server.accept();
            PrintWriter pout = new PrintWriter(client.getOutputStream(), true);
            System.out.println("Client is connected");
            pout.println(new java.util.Date().toString());

            client.close();
        }
    }
}
