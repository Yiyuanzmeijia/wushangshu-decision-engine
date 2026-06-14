def decide(position_correct, advantage, clarity):
    """
    Simple decision engine based on Wushangshu principles.
    """

    if not position_correct:
        return "Do not act"

    if advantage and clarity:
        return "Act immediately"

    if advantage and not clarity:
        return "Probe"

    return "Wait"


if __name__ == "__main__":
    decision = decide(position_correct=True, advantage=False, clarity=True)
    print("Decision:", decision)

---
