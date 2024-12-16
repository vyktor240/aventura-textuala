import java.util.Scanner;

public class TextAdventureGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Bine ai venit in Aventura Textuala!");
        System.out.println("Esti un aventurier curajos intr-un labirint misterios.");
        System.out.println("Obiectivul tau este sa gasesti comoara si sa scapi din labirint.");
        System.out.println("Fiecare alegere te va duce mai aproape de victorie... sau de pierzanie.");
        System.out.println("Mult noroc!\n");

        // Incepem povestea
        startGame(scanner);

        scanner.close();
    }

    public static void startGame(Scanner scanner) {
        System.out.println("Te trezesti la intrarea unui labirint intunecat.");
        System.out.println("Ai doua drumuri in fata: unul la STANGA si unul la DREAPTA.");
        System.out.print("Ce alegi? (scrie 'stanga' sau 'dreapta'): ");

        String choice = scanner.nextLine().trim().toLowerCase();

        if (choice.equals("stanga")) {
            goLeft(scanner);
        } else if (choice.equals("dreapta")) {
            goRight(scanner);
        } else {
            System.out.println("Alegere invalida. Te rog sa scrii 'stanga' sau 'dreapta'.");
            startGame(scanner);
        }
    }

    public static void goLeft(Scanner scanner) {
        System.out.println("\nAi luat drumul spre stanga. Drumul e stramt si intunecat.");
        System.out.println("Dupa cativa pasi, vezi un cufar pe jos.");
        System.out.print("Vrei sa-l DESCHIZI sau sa CONTINUI? (scrie 'deschide' sau 'continua'): ");

        String choice = scanner.nextLine().trim().toLowerCase();

        if (choice.equals("deschide")) {
            System.out.println("\nCufarul era o capcana! Ai fost atacat de o creatura monstruoasa.");
            System.out.println("Din pacate, ai pierdut jocul. Mai mult noroc data viitoare!");
        } else if (choice.equals("continua")) {
            System.out.println("\nAi ignorat cufarul si ai continuat. Gasesti o scara care duce in jos.");
            System.out.println("Cobori pe scara si gasesti comoara! Felicitari, ai castigat jocul!");
        } else {
            System.out.println("Alegere invalida. Te rog sa scrii 'deschide' sau 'continua'.");
            goLeft(scanner);
        }
    }

    public static void goRight(Scanner scanner) {
        System.out.println("\nAi luat drumul spre dreapta. Drumul e larg si bine luminat.");
        System.out.println("La capatul drumului vezi o usa masiva din lemn.");
        System.out.print("Vrei sa BATI la usa sau sa o IGNORI? (scrie 'bati' sau 'ignora'): ");

        String choice = scanner.nextLine().trim().toLowerCase();

        if (choice.equals("bati")) {
            System.out.println("\nUsa se deschide si un rege fantoma te invita inauntru.");
            System.out.println("Iti ofera comoara si un ospat regal. Felicitari, ai castigat jocul!");
        } else if (choice.equals("ignora")) {
            System.out.println("\nAi ignorat usa si te-ai intors la intrarea labirintului.");
            System.out.println("Din pacate, ai ratat sansa de a gasi comoara. Jocul s-a terminat.");
        } else {
            System.out.println("Alegere invalida. Te rog sa scrii 'bati' sau 'ignora'.");
            goRight(scanner);
        }
    }
}
