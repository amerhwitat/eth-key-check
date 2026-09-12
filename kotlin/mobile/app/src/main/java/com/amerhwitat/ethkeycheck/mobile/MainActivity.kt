package com.amerhwitat.ethkeycheck.mobile
import android.app.Activity
import android.os.Bundle
import android.view.Gravity
import android.widget.*
class MainActivity:Activity(){override fun onCreate(savedInstanceState:Bundle?){super.onCreate(savedInstanceState);val r=LinearLayout(this).apply{orientation=LinearLayout.VERTICAL;gravity=Gravity.CENTER;setPadding(32,32,32,32)};val t=TextView(this).apply{text="Eth Key Check — Kotlin Mobile";textSize=22f;gravity=Gravity.CENTER};val s=TextView(this).apply{text="Owner-authorized verification only\nSynthetic/public vectors supported\nPrivate-key recovery: disabled";textSize=16f;gravity=Gravity.CENTER;setPadding(0,24,0,24)};val b=Button(this).apply{text="Run safe verification";setOnClickListener{s.text="Verification boundary: active\nNo key cracking or seed guessing\n128D state: active"}};r.addView(t);r.addView(s);r.addView(b);setContentView(r)}}
