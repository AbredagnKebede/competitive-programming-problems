class Solution:
    def compress(self, chars: List[str]) -> int:
        curr_char = chars[0]
        curr_count = 1
        write_idx = 0
        
        for i in range(1, len(chars)):
            if chars[i] == curr_char:
                curr_count += 1
            else:
                chars[write_idx] = curr_char
                write_idx += 1
                if curr_count > 1:
                    for digit in str(curr_count):
                        chars[write_idx] = digit
                        write_idx += 1
                curr_char = chars[i]
                curr_count = 1
        
        chars[write_idx] = curr_char
        write_idx += 1
        if curr_count > 1:
            for digit in str(curr_count):
                chars[write_idx] = digit
                write_idx += 1

        return write_idx