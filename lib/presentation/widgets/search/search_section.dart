import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:perflexity/presentation/widgets/search/search_box.dart';

class SearchSection extends StatelessWidget {
  const SearchSection({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text(
          'AI-Powered Search',
          style: GoogleFonts.ibmPlexMono(
            fontSize: 40,
            fontWeight: FontWeight.w400,
            height: 1.2,
            letterSpacing: -0.5,
          ),
        ),
        const SizedBox(height: 32),
        SearchBox(),
      ],
    );
  }
}
