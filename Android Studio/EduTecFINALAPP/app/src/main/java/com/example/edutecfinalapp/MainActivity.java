package com.example.edutecfinalapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private EditText etn, etp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_inicio);

        etn = (EditText) findViewById(R.id.txt_nombre);
        etp = (EditText) findViewById(R.id.txt_password);

        Button button = (Button) findViewById(R.id.button);
        button.setOnClickListener(view -> Registrar());

    }

    private void Registrar() {
        String nombre = etn.getText().toString();
        String passward = etp.getText().toString();
        if (nombre.length() == 0) {
            Toast.makeText(this, "Debes de ingresar un nombre", Toast.LENGTH_LONG).show();
        }
        if (passward.length() == 0) {
            Toast.makeText(this, "Debes de ingresar una password", Toast.LENGTH_LONG).show();
        }
        if (etn.getText().toString().equals("admin") && etp.getText().toString().equals("admin")) {
            Toast.makeText(this, "Ingresando...", Toast.LENGTH_LONG).show();
            Intent siguiente = new Intent(this, Menu.class);
            startActivity(siguiente);

        } else {
            Toast.makeText(this, "error usuario y contraseña incorrectos", Toast.LENGTH_LONG).show();
        }
    }

    public void Registrar(View view) {
        String nombre = etn.getText().toString();
        String passward = etp.getText().toString();
        if (nombre.length() == 0) {
            Toast.makeText(this, "Debes de ingresar un nombre", Toast.LENGTH_LONG).show();
        }
        if (passward.length() == 0) {
            Toast.makeText(this, "Debes de ingresar una password", Toast.LENGTH_LONG).show();
        }
        if (etn.getText().toString().equals("admin") && etp.getText().toString().equals("admin")) {
            Toast.makeText(this, "Ingresando...", Toast.LENGTH_LONG).show();
            Intent siguiente = new Intent(this, Menu.class);
            startActivity(siguiente);

        } else {
            Toast.makeText(this, "error usuario y contraseña incorrectos", Toast.LENGTH_LONG).show();
        }
    }
    }

    //Metodo para el botón

