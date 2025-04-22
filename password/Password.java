package password;
import java.util.Random;
public class Password {
    private int passwordLength; // length of the password
    private String rawCharacters; // raw characters
    // initialize the password length and the raw character set
    public Password(int passwordLength) {
        this.passwordLength = passwordLength;
        this.rawCharacters = CharacterSet.NUMBER + CharacterSet.UPPER_CASE + CharacterSet.LOWER_CASE + CharacterSet.SPECIAL;
    }
    // generate and get the password
    public String getPassword() {
        Random random = new Random();
        String password = "";
        for(int i = 0; i < this.passwordLength; i++) {
            password += Character.toString(this.rawCharacters.charAt(random.nextInt(this.rawCharacters.length())));
        }
        return password;
    }
}