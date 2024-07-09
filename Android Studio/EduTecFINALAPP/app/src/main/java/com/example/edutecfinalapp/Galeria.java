package com.example.edutecfinalapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class Galeria extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_galeria);

        Button button = (Button) findViewById(R.id.button);
        button.setOnClickListener(view -> Salir());
    }

    private void Salir() {
        Intent siguiente = new Intent (this, MainActivity.class);
        startActivity(siguiente);
        Toast.makeText(this, "Dirigiendote al inicio", Toast.LENGTH_LONG).show();
    }

    public void Salir (View view)
    {
        Intent siguiente = new Intent (this, MainActivity.class);
        startActivity(siguiente);
        Toast.makeText(this, "Dirigiendote al inicio", Toast.LENGTH_LONG).show();
    }
}