import sys
sys.path.append('/home/root/python-packages')
sys.path.insert(0, '/home/root/python_packages')

import cv2
from ultralytics import YOLO
import time 

class YOLOTracker:
    def __init__(self, model_path, output_file):
        """
        Initialize YOLO tracker for camera input
        
        Args:
            model_path: Path to YOLO model weights
            output_file: Text file to store invisible object class indices
        """
        print("Loading YOLO model...")
        self.model = YOLO(model_path)
        self.output_file = output_file
        
        # Dictionary to keep track of active tracks and their class indices
        self.active_tracks = {}  # {track_id: class_idx}
        self.previous_tracks = set()  # Set of track IDs from previous frame
        
        # Statistics
        self.total_invisible_objects = 0
        self.class_invisible_count = 0

        self.class_mapping = {
            0: 'Longitudinal Crack',
            1: 'Transverse Crack',
            2: 'Aligator Crack',
            3: 'Other Corruption',
            4: 'Pothole'
        }
        print(f"YOLO model loaded successfully!")
    
    def log_invisible_object(self,track_id, class_idx):
        """Log invisible object to text file"""
        with open(self.output_file, 'a') as f:
            f.write(f"Object {track_id} :{self.class_mapping[class_idx]}\n")
        
        # Update statistics
        self.total_invisible_objects += 1
        self.class_invisible_count += 1
    
    def process_frame(self, frame):
        """
        Process a single frame for tracking
        
        Args:
            frame: Input frame (numpy array)
            
        Returns:
            annotated_frame: Frame with tracking annotations
        """
        start_time = time.time()

        # Run YOLO tracking
        results = self.model.track(frame, persist=True, verbose=False,tracker = "bytetrack.yaml")

        processing_time = time.time() - start_time
        
        # Get current frame's track IDs
        current_tracks = set()
        
        if results[0].boxes is not None and results[0].boxes.id is not None:
            # Extract tracking information
            boxes = results[0].boxes
            track_ids = boxes.id.int().cpu().tolist()
            class_indices = boxes.cls.int().cpu().tolist()
            
            # Update active tracks
            for track_id, class_idx in zip(track_ids, class_indices):
                current_tracks.add(track_id)
                self.active_tracks[track_id] = class_idx
        
        # Find tracks that became invisible (were in previous frame but not in current)
        invisible_tracks = self.previous_tracks - current_tracks
        
        # Log invisible objects
        for track_id in invisible_tracks:
            if track_id in self.active_tracks:
                class_idx = self.active_tracks[track_id]
                self.log_invisible_object(track_id,class_idx)
                # Remove from active tracks
                del self.active_tracks[track_id]
        
        # Update previous tracks for next iteration
        self.previous_tracks = current_tracks.copy()
        
        # Get annotated frame
        annotated_frame = results[0].plot()
        
        return annotated_frame, processing_time
    
    def track_from_camera(self, camera_index=0):
        """
        Track objects from camera feed
        
        Args:
            camera_index: Index of the camera to use (default 0)
        """
        cap = cv2.VideoCapture(camera_index)
        
        if not cap.isOpened():
            print(f"❌ Error: Could not open camera {camera_index}!")
            return
        
        print(f"\n🚀 Starting camera tracking...")
        print("Press 'q' to quit...")
        
        # prev_frame_time = 0
        # new_frame_time = 0
        # fps = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error reading frame from camera!")
                break
            
            # Process frame
            annotated_frame , processing_time= self.process_frame(frame)

            # new_frame_time = time.time()
            # fps = 1 / (new_frame_time - prev_frame_time)
            # prev_frame_time = new_frame_time
            
            # cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 30), 
                    #    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # cv2.putText(annotated_frame, f"Processing: {processing_time*1000:.1f}ms", (10, 70), 
                    #    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # Display the frame
            # cv2.imshow('YOLO Object Tracking', annotated_frame)
            
            # Break the loop if 'q' is pressed
            # if cv2.waitKey(1) & 0xFF == ord('q'):
                # break
        
        # Cleanup
        # cap.release()
        # cv2.destroyAllWindows()
        print("\n🎉 Tracking complete!")

# Initialize tracker
print("🔄 Initializing YOLO Tracker...")
tracker = YOLOTracker(model_path='./model_int8_openvino_model_H', output_file=r'/home/root/main_app/ai.txt')

# Start tracking from camera
tracker.track_from_camera()
