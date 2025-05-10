from emotion_detection import emotion_detector

def test_emotion_detector():
    """Test the emotion detector function with various emotion examples"""
 
    test_cases = [
        {"text": "I am glad this happened", "expected": "joy"},
        {"text": "I am really mad about this", "expected": "anger"},
        {"text": "I feel disgusted just hearing about this", "expected": "disgust"},
        {"text": "I am so sad about this", "expected": "sadness"},
        {"text": "I am really afraid that this will happen", "expected": "fear"}
    ]
    

    for i, test in enumerate(test_cases, 1):
        text = test["text"]
        expected = test["expected"]
        
        print(f"Test case {i}: Testing '{text}'")
        result = emotion_detector(text)
       
        assert result['dominant_emotion'] == expected, \
            f"Failed: Expected '{expected}', got '{result['dominant_emotion']}'"
        
        print(f"✓ Passed: Detected '{result['dominant_emotion']}' correctly\n")
    
    print("All test cases passed successfully!")

if __name__ == "__main__":
    test_emotion_detector()