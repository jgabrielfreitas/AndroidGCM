package jgabrielfreitas.androidgcm;

import android.app.Application;

import com.parse.Parse;
import com.parse.ParseObject;

/**
 * Created by JGabrielFreitas on 27/01/16.
 */
public class GcmApplication extends Application {

    public void onCreate() {
        super.onCreate();
        Parse.initialize(this, "m5iHVUqFIP2B34D1zcpYbDpD2eLTlrrzgWrFVfqc", "kk6zQ898kGFotDZuk2I20nW0ofNqIPtPcmcaFPLD");
    }
}
