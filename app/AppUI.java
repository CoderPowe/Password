package app;
import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JTextArea;
import javax.swing.JOptionPane;
public class AppUI {
   // declare and define widgets here
   private JFrame appWindow; // main app window
   private JButton generateButton; // generate button
   private JTextArea passwordField; // where the password will be shown
   public AppUI() {
      this.appWindow = new JFrame();
      this.appWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      this.appWindow.setLayout(null);
      this.generateButton = new JButton("Generate");
      this.generateButton.setBounds(600, 300, 100, 30);
      this.passwordField = new JTextArea();
      this.passwordField.setBounds(500, 200, 300, 30);
      this.appWindow.add(this.generateButton);
      this.appWindow.add(this.passwordField);
      this.appWindow.setVisible(true);// show the window
   }
   public JButton getGenerateButton() {
      return this.generateButton;
   }
   public JTextArea getPasswordField() {
      return this.passwordField;
   }
   public static String getInput() {
      return JOptionPane.showInputDialog("Length: ");
   }
}