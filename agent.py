class AttendanceAgent:
    """
    AI Agent for Student Attendance & Performance Monitoring
    """

    def __init__(self, model, encoder):
        self.model = model
        self.encoder = encoder

    def perceive(self, input_data):
        """
        Step 1: Perception using ML model
        """
        encoded_prediction = self.model.predict(input_data)[0]
        risk = self.encoder.inverse_transform([encoded_prediction])[0]
        return risk

    def decide(self, risk):
        """
        Step 2: Decision making
        """
        if risk == "Safe":
            return {
                "action": "Monitor",
                "message": "Student performance is stable. Continue current efforts."
            }

        elif risk == "At Risk":
            return {
                "action": "Warn",
                "message": "Student is at risk. Improve attendance and assignment completion."
            }

        else:
            return {
                "action": "Escalate",
                "message": "Critical academic risk detected. Immediate mentor intervention required."
            }

    def act(self, decision):
        """
        Step 3: Action execution
        """
        return decision
