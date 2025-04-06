import cv2
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import os

def record_video(duration=15):
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('fire_detection.avi', fourcc, 20.0, (640, 480))
    
    start_time = time.time()
    while int(time.time() - start_time) < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            print("Failed to capture frame for recording.")
            break
    
    cap.release()
    out.release()

def send_email_alert():
    sender_email = "mydemo553@gmail.com"
    receiver_email = "hesek82848@sgatra.com"
    password = "occq fmum ivbv upzu"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Emergency Alert: Fire Detected"

    body = "🔥Fire has been detected in the classroom No. 7... Please take immediate action.🔥"
    message.attach(MIMEText(body, 'plain'))

    filename = "fire_detection.avi"
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename={filename}")

    message.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Alert email with video attachment sent successfully.")
    except Exception as e:
        print(f"Failed to send email alert: {e}")
    finally:
        server.quit()
        attachment.close()
        os.remove(filename)  # Remove the video file after sending

def detect_fire(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_bound = np.array([18, 50, 50])
    upper_bound = np.array([35, 255, 255])
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
    detected = np.count_nonzero(mask)
    return detected > 5000

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use DirectShow backend
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    alert_triggered = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        if detect_fire(frame):
            cv2.putText(frame, "Fire Detected!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if not alert_triggered:
                print("Fire detected! Recording video...")
                record_video()
                send_email_alert()
                alert_triggered = True
        
        cv2.imshow("Fire Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
