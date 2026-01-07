import math
from typing import Tuple

class ContinuityIndexToolkit:
    """
    Continuity Index (CI) v2.0 Toolkit

    A Python toolkit for measuring informational persistence and extinction risk in complex systems,
    based on Information Continuity Theory (ICT).

    Core Formula:
        CI = (R × f_I) / (λ × d_I)
        log_CI = log10(CI)

    Where:
        R       : Reproduction rate (ability to generate viable successors)
        f_I     : Fidelity (preservation of essential information/structure in successors)
        d_I     : Deletion hazard (likelihood of failure or loss per unit time)
        lambda_env : Volatility multiplier (turbulence / instability in the environment)

    Minimal Interpretation:
        - CI > 1  (log_CI > 0) : Effective continuity; system tends to persist/grow.
        - CI = 1  (log_CI = 0) : Fragile equilibrium.
        - CI < 1  (log_CI < 0) : Continuity fails in expectation; extinction/collapse risk is high.

    Rich Regime Bands (CI v2.0 style, based on log_CI):
        - log_CI ≥ 4.0 : super_persistent
        - 2.0 ≤ log_CI < 4.0 : strong
        - 1.0 ≤ log_CI < 2.0 : fragile
        - log_CI < 1.0 : collapse_gravity
    """

    # ---------- Core calculation ----------

    def calculate_ci(self, R: float, f_I: float, d_I: float, lambda_env: float) -> Tuple[float, float]:
        """
        Calculate the Continuity Index (CI) and its log10 value.

        Args:
            R (float): Reproduction rate (>= 0).
            f_I (float): Fidelity (>= 0, typically in [0, 1]).
            d_I (float): Deletion hazard (>= 0).
            lambda_env (float): Volatility multiplier (>= 0).

        Returns:
            (CI, log_CI): Tuple[float, float]

        Raises:
            ValueError: If denominator is zero or any input is invalid.
        """
        for name, x in [("R", R), ("f_I", f_I), ("d_I", d_I), ("lambda_env", lambda_env)]:
            if not isinstance(x, (int, float)):
                raise ValueError(f"{name} must be a number.")
            if x < 0:
                raise ValueError(f"{name} must be non-negative.")

        denominator = lambda_env * d_I
        if denominator == 0:
            raise ValueError("Denominator (λ × d_I) cannot be zero (would cause division by zero).")

        ci = (R * f_I) / denominator
        log_ci = math.log10(ci) if ci > 0 else float("-inf")
        return ci, log_ci

    # ---------- Minimal threshold interpretation ----------

    def interpret_ci_minimal(self, ci: float) -> str:
        """
        Provide a minimal interpretation of the CI value using the CI > 1 threshold.

        Args:
            ci (float): Continuity Index.

        Returns:
            str: Interpretation string.
        """
        if ci > 1:
            return "The system is on a path to persist and potentially grow (effective continuity)."
        elif ci == 1:
            return "The system is in a fragile equilibrium; small changes can shift it toward growth or collapse."
        elif ci < 1:
            return "The system is at risk of collapse or extinction in expectation (continuity threshold not met)."
        else:
            return "Invalid CI value."

    # ---------- Rich regime bands (CI v2.0) ----------

    def classify_regime(self, log_ci: float) -> str:
        """
        Classify continuity regime based on log_CI using CI v2.0 bands.

        Args:
            log_ci (float): log10(CI)

        Returns:
            str: One of {"super_persistent", "strong", "fragile", "collapse_gravity"}.
        """
        if log_ci >= 4:
            return "super_persistent"
        elif log_ci >= 2:
            return "strong"
        elif log_ci >= 1:
            return "fragile"
        else:
            return "collapse_gravity"

    def explain_regime(self, log_ci: float) -> str:
        """
        Provide a human-readable explanation of the regime classification.

        Args:
            log_ci (float): log10(CI)

        Returns:
            str: Explanation of the system's continuity status.
        """
        regime = self.classify_regime(log_ci)

        if regime == "super_persistent":
            return (
                "System exhibits very strong continuity (super_persistent): "
                "it is structurally robust and highly likely to persist barring extreme, nonlocal shocks."
            )
        elif regime == "strong":
            return (
                "System has strong continuity: it is generally robust and resilient, "
                "but still worth monitoring for long-term drift or accumulating stress."
            )
        elif regime == "fragile":
            return (
                "System is in the fragile continuity band: continuity may hold for some time, "
                "but relatively modest shocks or parameter changes can push it toward collapse or recovery."
            )
        else:  # collapse_gravity
            return (
                "System is in the collapse-gravity regime: without significant intervention to improve reproduction, "
                "fidelity, or reduce hazard/volatility, continuity is unlikely to be sustained."
            )

# Example usage
if __name__ == "__main__":
    toolkit = ContinuityIndexToolkit()
    try:
        ci, log_ci = toolkit.calculate_ci(R=2.5, f_I=0.8, d_I=0.1, lambda_env=1.2)
        print(f"CI: {ci:.4f}")
        print(f"log_CI: {log_ci:.4f}")
        print("Minimal interpretation:", toolkit.interpret_ci_minimal(ci))
        regime = toolkit.classify_regime(log_ci)
        print("Regime label:", regime)
        print("Regime explanation:", toolkit.explain_regime(log_ci))
    except ValueError as e:
        print(f"Error: {e}")
