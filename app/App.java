package app;
import password.Password;
import java.awt.*;
import java.awt.event.*;
public class App {
    
    private AppUI appUI; // app ui
    public App() {
      this.appUI = new AppUI();
    }
    public void start() {
      // main app logic here
      appUI.getGenerateButton().addActionListener(new ActionListener(){
        @Override
        public void actionPerformed(ActionEvent e) {
            // input dialog
            int passwordLength = Integer.parseInt(AppUI.getInput());
            App.this.appUI.getPasswordField().setText(new Password(passwordLength).getPassword());
        }
      });
    }
}