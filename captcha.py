import com.DeathByCaptcha.AccessDeniedException;
import com.DeathByCaptcha.Captcha;
import com.DeathByCaptcha.Client;
import com.DeathByCaptcha.SocketClient;
import com.DeathByCaptcha.HttpClient;

/* Put your DeathByCaptcha account username and password here.
   Use HttpClient for HTTP API. */
username='gaurangsharma'
password='Gauri@123'
Client client = (Client)new SocketClient(username, password);
try {
    double balance = client.getBalance();

    /* Put your CAPTCHA file name, or file object, or arbitrary input stream,
       or an array of bytes, and optional solving timeout (in seconds) here: */
    captchaFileName=http://www.mca.gov.in/mcafoportal/login.do/mcafoportal/getCapchaImage.do
    timeout=30
    Captcha captcha = client.decode(captchaFileName, timeout);
    if (null != captcha) {
        /* The CAPTCHA was solved; captcha.id property holds its numeric ID,
           and captcha.text holds its text. */
        System.out.println("CAPTCHA " + captcha.id + " solved: " + captcha.text);

        if (/* check if the CAPTCHA was incorrectly solved */) {
            client.report(captcha);
        }
    }
} catch (AccessDeniedException e) {
    /* Access to DBC API denied, check your credentials and/or balance */
}