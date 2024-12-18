from typing import List, Dict, Union


class CircuitParser:
    def __init__(self):
        self.circuit: List[Dict[str, Union[str, Dict]]] = []

    def parse_netlist(self, file_path: str):

        sub_circuit = {
            "transistor": [],
            "resistor": [],
            "module": []
        }

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith(('*', '.')) or not line:
                        continue

                    if line.startswith("M"):
                        element = self._parse_transistor(line)
                        sub_circuit["transistor"].append(element)
                    elif line.startswith("xr"):
                        element = self._parse_resistor(line)
                        sub_circuit["resistor"].append(element)
                    elif line.startswith("X"):
                        element = self._parse_module(line)
                        sub_circuit["module"].append(element)

            self.circuit.append({"sub_circuit": sub_circuit})

        except FileNotFoundError:
            print(f"Fail {file_path} not found.")
        except Exception as e:
            print(f"Parse error : {e}")

    def _parse_transistor(self, line: str) -> Dict:

        parts = line.split()
        name = parts[0]
        parameters = self._extract_parameters(parts[1:])
        return {"name": name, "type": "transistor", "parameters": parameters}

    def _parse_resistor(self, line: str) -> Dict:

        parts = line.split()
        name = parts[0]
        parameters = self._extract_parameters(parts[1:])
        return {"name": name, "type": "resistor", "parameters": parameters}

    def _parse_module(self, line: str) -> Dict:

        parts = line.split()
        name = parts[0]
        parameters = self._extract_parameters(parts[1:])
        return {"name": name, "type": "module", "parameters": parameters}

    def _extract_parameters(self, parts: List[str]) -> Dict:

        parameters = {}
        for idx, part in enumerate(parts):
            if '=' in part:
                key, value = part.split('=', 1)
                parameters[key] = value
            else:
                parameters[f"positional_{idx}"] = part
        return parameters

    def write_netlist(self, file_path: str):
        try:
            with open(file_path, 'w') as file:
                for sub in self.circuit:
                    sub_circuit = sub["sub_circuit"]

                    for element_type, elements in sub_circuit.items():
                        for element in elements:
                            line = self._format_element(element)
                            file.write(line + '\n')

        except Exception as e:
            print(f"Error : {e}")

    def _format_element(self, element: Dict) -> str:

        name = element["name"]
        params = " ".join(
            f"{k}={v}" if "positional" not in k else v
            for k, v in element["parameters"].items()
        )
        return f"{name} {params}"

if __name__ == "__main__":
    parser = CircuitParser()
    parser.parse_netlist("opamp_netlist.txt")
    print("Parsed Circuit Structure:", parser.circuit)
    parser.write_netlist("output_netlist.txt")
