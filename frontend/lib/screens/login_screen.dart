import 'package:flutter/material.dart';
import '../constants/app_colors.dart';
import '../constants/app_text_styles.dart';
import '../widgets/custom_button.dart';
import '../widgets/custom_text_field.dart';
import 'signup_screen.dart';

class LoginScreen extends StatelessWidget {
  const LoginScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Connexion"),
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const SizedBox(height: 20),

              const Text(
                "Bon retour 👋",
                style: AppTextStyles.heading,
              ),

              const SizedBox(height: 10),

              const Text(
                "Connectez-vous pour accéder à votre assistant médical intelligent.",
                style: AppTextStyles.bodySecondary,
              ),

              const SizedBox(height: 40),

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
                hintText: "Entrez votre mot de passe",
                icon: Icons.lock_outline,
                obscureText: true,
              ),

              const SizedBox(height: 14),

              Align(
                alignment: Alignment.centerRight,
                child: TextButton(
                  onPressed: () {},
                  child: const Text(
                    "Mot de passe oublié ?",
                    style: TextStyle(
                      color: AppColors.primary,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                ),
              ),

              const SizedBox(height: 20),

              CustomButton(
                text: "Se connecter",
                onPressed: () {
                  // Connexion backend plus tard
                },
              ),

              const SizedBox(height: 20),

              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text(
                    "Vous n'avez pas de compte ? ",
                    style: AppTextStyles.bodySecondary,
                  ),
                  GestureDetector(
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => const SignupScreen(),
                        ),
                      );
                    },
                    child: const Text(
                      "Créer un compte",
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