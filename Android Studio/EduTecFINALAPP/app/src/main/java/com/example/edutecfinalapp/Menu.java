package com.example.edutecfinalapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class Menu extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        Button button = (Button) findViewById(R.id.button);
            button.setOnClickListener(view -> IrGaleria());
        Button button2 = (Button) findViewById(R.id.button2);
            button2.setOnClickListener(view -> IrNavegador());
        Button button3 = (Button) findViewById(R.id.button3);
            button3.setOnClickListener(view -> IrInfo());
        Button button8 = (Button) findViewById(R.id.button8);
            button8.setOnClickListener(view -> Salida());
    }

    private void Salida() {
        Intent siguiente = new Intent(this, MainActivity.class);
        startActivity(siguiente);
        Toast.makeText(this, "Dirigiendote al inicio", Toast.LENGTH_LONG).show();
    }

    private void IrNavegador() {
        Intent siguiente = new Intent(this, Navegador.class);
        startActivity(siguiente);
        Toast.makeText(this, "Dirigiendote al navegador", Toast.LENGTH_LONG).show();
    }

    private void IrInfo() {
        Intent siguiente = new Intent(this, Informacion.class);
        startActivity(siguiente);
        Toast.makeText(this, "Dirigiendote a información", Toast.LENGTH_LONG).show();
    }

    private void IrGaleria() {
        Intent siguiente = new Intent(this, Galeria.class);
        startActivity(siguiente);
        Toast.makeText(this, "Dirigiendote a la galería", Toast.LENGTH_LONG).show();
    }

    public void IrGaleria (View view)
    {
        Intent siguiente = new Intent(this, Galeria.class);
        startActivity(siguiente);
        Toast.makeText(this, "Dirigiendote a información a la galería", Toast.LENGTH_LONG).show();
    }

    public void IrInfo (View view)
    {
        Intent siguiente = new Intent(this, Informacion.class);
        startActivity(siguiente);
        Toast.makeText(this, "Dirigiendote a información", Toast.LENGTH_LONG).show();
    }

    public void IrNavegador (View view)
    {
        Intent siguiente = new Intent(this, Navegador.class);
        startActivity(siguiente);
        Toast.makeText(this, "Dirigiendote al navegador", Toast.LENGTH_LONG).show();
    }

    public void Salida (View view)
    {
        Intent siguiente = new Intent(this, MainActivity.class);
        startActivity(siguiente);
        Toast.makeText(this, "Dirigiendote al inicio", Toast.LENGTH_LONG).show();
    }
}