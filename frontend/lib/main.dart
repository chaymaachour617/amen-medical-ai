import 'package:amen_app/constants/app_theme.dart';
import 'package:flutter/material.dart';
import 'screens/chat_screen.dart';

void main() {
  runApp(const AmenApp());
}

class AmenApp extends StatelessWidget {
  const AmenApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'AMEN',
      theme: AppTheme.lightTheme,
      home: const ChatScreen(),
    );
  }
}