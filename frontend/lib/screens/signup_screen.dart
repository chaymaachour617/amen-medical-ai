import 'package:flutter/material.dart';
import '../constants/app_colors.dart';
import '../constants/app_text_styles.dart';
import '../widgets/custom_button.dart';
import '../widgets/custom_text_field.dart';

class SignupScreen extends StatelessWidget {
  const SignupScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Créer un compte"),
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const SizedBox(height: 20),

              const Text(
                "Bienvenue 👋",
                style: AppTextStyles.heading,
              ),

              const SizedBox(height: 10),

              const Text(
                "Créez votre compte pour commencer à utiliser AMEN.",
                style: AppTextStyles.bodySecondary,
              ),

              const SizedBox(height: 40),

              const Text("Nom complet", style: AppTextStyles.body),
              const SizedBox(height: 8),

              const CustomTextField(
                hintText: "Entrez votre nom complet",
                icon: Icons.person_outline,
              ),

              const SizedBox(height: 20),

              const Text("Email", style: AppTextStyles.body),
              const SizedBox(height: 8),

              const CustomTextField(
                hintText: "Entrez votre email",
                icon: Icons.email_outlined,
                keyboardType: TextInputType.emailAddress,
              ),

              const SizedBox(height: 20),

              const Text("Mot de passe", style: AppTextStyles.body),
              const SizedBox(height: 8),

              const CustomTextField(
                hintText: "Créez un mot de passe",
                icon: Icons.lock_outline,
                obscureText: true,
              ),

              const SizedBox(height: 20),

              const Text("Confirmer le mot de passe", style: AppTextStyles.body),
              const SizedBox(height: 8),

              const CustomTextField(
                hintText: "Confirmez votre mot de passe",
                icon: Icons.lock_reset_outlined,
                obscureText: true,
              ),

              const SizedBox(height: 30),

              CustomButton(
                text: "Créer mon compte",
                onPressed: () {
                  // Inscription backend plus tard
                },
              ),

              const SizedBox(height: 20),

              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text(
                    "Vous avez déjà un compte ? ",
                    style: AppTextStyles.bodySecondary,
                  ),
                  GestureDetector(
                    onTap: () {
                      Navigator.pop(context);
                    },
                    child: const Text(
                      "Se connecter",
                      style: TextStyle(
                        color: AppColors.primary,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}