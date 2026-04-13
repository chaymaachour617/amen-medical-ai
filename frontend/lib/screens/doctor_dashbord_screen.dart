import 'package:flutter/material.dart';
import '../constants/app_colors.dart';
import '../widgets/stat_card.dart';
import '../widgets/patient_progress_card.dart';

class DoctorDashboardScreen extends StatelessWidget {
  const DoctorDashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: AppBar(
        title: const Text("Dashboard Médecin"),
        actions: [
          IconButton(
            onPressed: () {},
            icon: const Icon(Icons.notifications_none_rounded),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(18),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              "Bonjour Dr. AMEN 👋",
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
                color: AppColors.textPrimary,
              ),
            ),
            const SizedBox(height: 8),
            const Text(
              "Voici un aperçu de l’état et de la progression de vos patients.",
              style: TextStyle(
                fontSize: 14,
                color: AppColors.textSecondary,
              ),
            ),

            const SizedBox(height: 24),

            Row(
              children: const [
                StatCard(
                  title: "Patients suivis",
                  value: "24",
                  icon: Icons.people_alt_outlined,
                  color: AppColors.primary,
                ),
                StatCard(
                  title: "Patients stables",
                  value: "18",
                  icon: Icons.favorite_outline,
                  color: Colors.green,
                ),
              ],
            ),

            Row(
              children: const [
                StatCard(
                  title: "À risque",
                  value: "4",
                  icon: Icons.warning_amber_rounded,
                  color: Colors.orange,
                ),
                StatCard(
                  title: "Alertes",
                  value: "7",
                  icon: Icons.notifications_active_outlined,
                  color: Colors.red,
                ),
              ],
            ),

            const SizedBox(height: 26),

            const Text(
              "📈 Progression des patients",
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.w700,
                color: AppColors.textPrimary,
              ),
            ),

            const SizedBox(height: 16),

            const PatientProgressCard(
              name: "Ahmed Ben Ali",
              condition: "Diabète de type 2",
              progress: 80,
              status: "Stable",
              statusColor: Colors.green,
            ),

            const PatientProgressCard(
              name: "Salma Trabelsi",
              condition: "Hypertension",
              progress: 55,
              status: "Attention",
              statusColor: Colors.orange,
            ),

            const PatientProgressCard(
              name: "Youssef Gharbi",
              condition: "Régime nutritionnel",
              progress: 92,
              status: "Très bien",
              statusColor: Colors.blue,
            ),

            const SizedBox(height: 24),

            const Text(
              "🚨 Patients à surveiller",
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.w700,
                color: AppColors.textPrimary,
              ),
            ),

            const SizedBox(height: 14),

            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(18),
                border: Border.all(color: AppColors.border),
              ),
              child: Column(
                children: const [
                  ListTile(
                    contentPadding: EdgeInsets.zero,
                    leading: CircleAvatar(
                      backgroundColor: Color(0xFFFFF3E0),
                      child: Icon(Icons.warning_amber_rounded, color: Colors.orange),
                    ),
                    title: Text("Salma Trabelsi"),
                    subtitle: Text("Tension élevée cette semaine"),
                  ),
                  Divider(),
                  ListTile(
                    contentPadding: EdgeInsets.zero,
                    leading: CircleAvatar(
                      backgroundColor: Color(0xFFFFEBEE),
                      child: Icon(Icons.error_outline, color: Colors.red),
                    ),
                    title: Text("Hichem Mzoughi"),
                    subtitle: Text("Repas non adaptés détectés"),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}