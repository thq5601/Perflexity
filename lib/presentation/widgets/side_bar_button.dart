// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'package:flutter/material.dart';

import 'package:perflexity/theme/colors.dart';

class SideBarButton extends StatelessWidget {
  final bool isCollapsed;
  final IconData icon;
  final String text;
  const SideBarButton({
    super.key,
    required this.isCollapsed,
    required this.icon,
    required this.text,
  });

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment:
          isCollapsed ? MainAxisAlignment.center : MainAxisAlignment.start,
      children: [
        Container(
          margin: const EdgeInsets.symmetric(vertical: 14, horizontal: 18),
          child: Icon(icon, color: AppColors.iconGrey, size: 28),
        ),
        isCollapsed
            ? const SizedBox()
            : Expanded(
              child: Text(
                text,
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                overflow: TextOverflow.ellipsis,
                softWrap: false,
              ),
            ),
      ],
    );
  }
}
