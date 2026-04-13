import 'package:flutter/material.dart';
import '../constants/app_colors.dart';
import '../widgets/chat_bubble.dart';

class ChatScreen extends StatefulWidget {
  const ChatScreen({super.key});

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final TextEditingController _messageController = TextEditingController();

  final List<Map<String, dynamic>> messages = [
    {
      "text":
          "Bonjour 👋 Je suis votre assistant médical AMEN.\nJe peux vous aider avec vos symptômes, vos repas et vos questions de santé.",
      "isUser": false,
    },
  ];

  void sendMessage() {
    final text = _messageController.text.trim();

    if (text.isEmpty) return;

    setState(() {
      messages.add({
        "text": text,
        "isUser": true,
      });

      messages.add({
        "text":
            "Merci pour votre message. Cette réponse est simulée pour l’instant. Plus tard, elle viendra de votre backend IA.",
        "isUser": false,
      });
    });

    _messageController.clear();
  }

  void recordVoice() {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text("🎤 Enregistrement vocal bientôt disponible"),
      ),
    );
  }

  void takeFoodPhoto() {
    setState(() {
      messages.add({
        "text": "📷 J’ai pris une photo de mon plat",
        "isUser": true,
      });

      messages.add({
        "text":
            "🍽️ Analyse simulée :\nCe plat semble acceptable en quantité modérée.\nL’analyse réelle sera connectée plus tard avec l’IA.",
        "isUser": false,
      });
    });
  }

  void sendQuickMessage(String text) {
    setState(() {
      messages.add({
        "text": text,
        "isUser": true,
      });

      messages.add({
        "text":
            "Merci 👌 Je vais bientôt analyser cette demande avec l’intelligence artificielle médicale.",
        "isUser": false,
      });
    });
  }

  Widget quickAction(String title, IconData icon, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
        margin: const EdgeInsets.only(right: 10),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: AppColors.border),
        ),
        child: Row(
          children: [
            Icon(icon, size: 18, color: AppColors.primary),
            const SizedBox(width: 8),
            Text(
              title,
              style: const TextStyle(
                fontSize: 13,
                fontWeight: FontWeight.w600,
                color: AppColors.textPrimary,
              ),
            ),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        elevation: 0,
        title: Row(
          children: [
            Container(
              width: 38,
              height: 38,
              decoration: const BoxDecoration(
                shape: BoxShape.circle,
                color: AppColors.primary,
              ),
              child: const Icon(
                Icons.health_and_safety_rounded,
                color: Colors.white,
                size: 20,
              ),
            ),
            const SizedBox(width: 12),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text(
                  "AMEN Assistant",
                  style: TextStyle(fontSize: 16, fontWeight: FontWeight.w700),
                ),
                Text(
                  "En ligne",
                  style: TextStyle(
                    fontSize: 12,
                    color: AppColors.success,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
      body: Column(
        children: [
          // Actions rapides
          Container(
            padding: const EdgeInsets.only(top: 14, left: 16, right: 16),
            height: 78,
            child: ListView(
              scrollDirection: Axis.horizontal,
              children: [
                quickAction(
                  "Symptômes",
                  Icons.monitor_heart_outlined,
                  () => sendQuickMessage("Je veux analyser mes symptômes"),
                ),
                quickAction(
                  "Mon plat",
                  Icons.restaurant_menu_rounded,
                  () => sendQuickMessage("Puis-je manger ce plat ?"),
                ),
                quickAction(
                  "Vocal",
                  Icons.mic_rounded,
                  recordVoice,
                ),
                quickAction(
                  "Médecin",
                  Icons.local_hospital_outlined,
                  () => sendQuickMessage("Je veux parler à un médecin"),
                ),
              ],
            ),
          ),

          // Messages
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              itemCount: messages.length,
              itemBuilder: (context, index) {
                return ChatBubble(
                  message: messages[index]["text"],
                  isUser: messages[index]["isUser"],
                );
              },
            ),
          ),

          // Barre de saisie
          Container(
            padding: const EdgeInsets.fromLTRB(14, 10, 14, 18),
            decoration: const BoxDecoration(
              color: Colors.white,
              border: Border(
                top: BorderSide(color: AppColors.border),
              ),
            ),
            child: Row(
              children: [
                // Caméra
                Container(
                  decoration: BoxDecoration(
                    color: AppColors.secondary.withOpacity(0.12),
                    shape: BoxShape.circle,
                  ),
                  child: IconButton(
                    onPressed: takeFoodPhoto,
                    icon: const Icon(
                      Icons.camera_alt_rounded,
                      color: AppColors.secondary,
                    ),
                  ),
                ),

                const SizedBox(width: 10),

                // Champ texte
                Expanded(
                  child: TextField(
                    controller: _messageController,
                    decoration: InputDecoration(
                      hintText: "Écrivez votre message...",
                      filled: true,
                      fillColor: const Color(0xFFF8FAFC),
                      contentPadding: const EdgeInsets.symmetric(
                        horizontal: 18,
                        vertical: 14,
                      ),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(18),
                        borderSide: const BorderSide(color: AppColors.border),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(18),
                        borderSide: const BorderSide(color: AppColors.border),
                      ),
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(18),
                        borderSide: const BorderSide(
                          color: AppColors.primary,
                          width: 1.4,
                        ),
                      ),
                    ),
                  ),
                ),

                const SizedBox(width: 10),

                // Micro
                Container(
                  decoration: BoxDecoration(
                    color: AppColors.primary.withOpacity(0.12),
                    shape: BoxShape.circle,
                  ),
                  child: IconButton(
                    onPressed: recordVoice,
                    icon: const Icon(
                      Icons.mic_rounded,
                      color: AppColors.primary,
                    ),
                  ),
                ),

                const SizedBox(width: 10),

                // Envoyer
                Container(
                  decoration: const BoxDecoration(
                    color: AppColors.primary,
                    shape: BoxShape.circle,
                  ),
                  child: IconButton(
                    onPressed: sendMessage,
                    icon: const Icon(
                      Icons.send_rounded,
                      color: Colors.white,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}